use std::fmt;

use crate::prelude::*;

impl fmt::Display for Expr {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        fmt::Debug::fmt(self, f)
    }
}

impl fmt::Debug for Expr {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        use Expr::*;
        match self {
            Window {
                function,
                partition_by,
                order_by,
                options,
            } => match options {
                #[cfg(feature = "dynamic_group_by")]
                WindowType::Rolling(options) => {
                    write!(
                        f,
                        "{:?}.rolling(by='{}', offset={}, period={})",
                        function, options.index_column, options.offset, options.period
                    )
                },
                _ => {
                    if let Some((order_by, _)) = order_by {
                        write!(
                            f,
                            "{function:?}.over(partition_by: {partition_by:?}, order_by: {order_by:?})"
                        )
                    } else {
                        write!(f, "{function:?}.over({partition_by:?})")
                    }
                },
            },
            DataTypeFunction(dtype_fn) => fmt::Debug::fmt(dtype_fn, f),
            Len => write!(f, "len()"),
            Explode {
                input: expr,
                skip_empty: false,
            } => write!(f, "{expr:?}.explode()"),
            Explode {
                input: expr,
                skip_empty: true,
            } => write!(f, "{expr:?}.explode(skip_empty)"),
            Alias(expr, name) => write!(f, "{expr:?}.alias(\"{name}\")"),
            Column(name) => write!(f, "col(\"{name}\")"),
            Literal(v) => write!(f, "{v:?}"),
            BinaryExpr { left, op, right } => write!(f, "[({left:?}) {op:?} ({right:?})]"),
            Sort { expr, options } => {
                if options.descending {
                    write!(f, "{expr:?}.sort(desc)")
                } else {
                    write!(f, "{expr:?}.sort(asc)")
                }
            },
            SortBy {
                expr,
                by,
                sort_options,
            } => {
                write!(
                    f,
                    "{expr:?}.sort_by(by={by:?}, sort_option={sort_options:?})",
                )
            },
            Filter { input, by } => {
                write!(f, "{input:?}.filter({by:?})")
            },
            Gather {
                expr,
                idx,
                returns_scalar,
            } => {
                if *returns_scalar {
                    write!(f, "{expr:?}.get({idx:?})")
                } else {
                    write!(f, "{expr:?}.gather({idx:?})")
                }
            },
            SubPlan(lf, _) => {
                write!(f, ".subplan({lf:?})")
            },
            Agg(agg) => {
                use AggExpr::*;
                match agg {
                    Min {
                        input,
                        propagate_nans,
                    } => {
                        if *propagate_nans {
                            write!(f, "{input:?}.nan_min()")
                        } else {
                            write!(f, "{input:?}.min()")
                        }
                    },
                    Max {
                        input,
                        propagate_nans,
                    } => {
                        if *propagate_nans {
                            write!(f, "{input:?}.nan_max()")
                        } else {
                            write!(f, "{input:?}.max()")
                        }
                    },
                    Median(expr) => write!(f, "{expr:?}.median()"),
                    Mean(expr) => write!(f, "{expr:?}.mean()"),
                    First(expr) => write!(f, "{expr:?}.first()"),
                    Last(expr) => write!(f, "{expr:?}.last()"),
                    Implode(expr) => write!(f, "{expr:?}.list()"),
                    NUnique(expr) => write!(f, "{expr:?}.n_unique()"),
                    Sum(expr) => write!(f, "{expr:?}.sum()"),
                    AggGroups(expr) => write!(f, "{expr:?}.groups()"),
                    Count(expr, _) => write!(f, "{expr:?}.count()"),
                    Var(expr, _) => write!(f, "{expr:?}.var()"),
                    Std(expr, _) => write!(f, "{expr:?}.std()"),
                    Quantile { expr, .. } => write!(f, "{expr:?}.quantile()"),
                }
            },
            Cast {
                expr,
                dtype,
                options,
            } => {
                if options.is_strict() {
                    write!(f, "{expr:?}.strict_cast({dtype:?})")
                } else {
                    write!(f, "{expr:?}.cast({dtype:?})")
                }
            },
            Ternary {
                predicate,
                truthy,
                falsy,
            } => write!(
                f,
                ".when({predicate:?}).then({truthy:?}).otherwise({falsy:?})",
            ),
            Function { input, function } => {
                if input.len() >= 2 {
                    write!(f, "{:?}.{function}({:?})", input[0], &input[1..])
                } else {
                    write!(f, "{:?}.{function}()", input[0])
                }
            },
            AnonymousFunction {
                input,
                fmt_str,
                function,
                ..
            } => {
                let name = match function {
                    LazySerde::Named { name, .. } => name.as_str(),
                    _ => fmt_str.as_str(),
                };

                if input.len() >= 2 {
                    write!(f, "{:?}.{}({:?})", input[0], name, &input[1..])
                } else {
                    write!(f, "{:?}.{}()", input[0], name)
                }
            },
            Eval {
                expr: input,
                evaluation,
                variant,
            } => match variant {
                EvalVariant::List => write!(f, "{input:?}.list.eval({evaluation:?})"),
                EvalVariant::Cumulative { min_samples } => write!(
                    f,
                    "{input:?}.Cumulative_eval({evaluation:?}, min_samples={min_samples}"
                ),
            },
            Slice {
                input,
                offset,
                length,
            } => write!(f, "{input:?}.slice(offset={offset:?}, length={length:?})",),
            KeepName(e) => write!(f, "{e:?}.name.keep()"),
            RenameAlias { expr, function } => match function {
                RenameAliasFn::Prefix(s) => write!(f, "{expr:?}.prefix({s})"),
                RenameAliasFn::Suffix(s) => write!(f, "{expr:?}.suffix({s})"),
                RenameAliasFn::ToLowercase => write!(f, "{expr:?}.to_lowercase()"),
                RenameAliasFn::ToUppercase => write!(f, "{expr:?}.to_uppercase()"),
                #[cfg(feature = "python")]
                RenameAliasFn::Python(_) => write!(f, "{expr:?}.rename_alias()"),
                RenameAliasFn::Rust(_) => write!(f, "{expr:?}.rename_alias()"),
            },
            Selector(s) => fmt::Display::fmt(s, f),
            #[cfg(feature = "dtype-struct")]
            Field(names) => write!(f, "pl.field({names:?})"),
        }
    }
}
