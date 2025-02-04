window.SIDEBAR_ITEMS = {"constant":["IDX_DTYPE","NULL","URL_ENCODE_CHAR_SET"],"enum":["AggExpr","Ambiguous","AnyValue","ArrowDataType","ArrowTimeUnit","AsofStrategy","BooleanFunction","CategoricalFunction","CategoricalOrdering","ClosedInterval","ClosedWindow","Column","CommentPrefix","CsvEncoding","DataType","DslPlan","Excluded","Expr","FillNullStrategy","FunctionExpr","GroupByMethod","GroupsIndicator","GroupsType","IndexOrder","InequalityOperator","InterpolationMethod","IpcCompression","JoinCoalesce","JoinType","JoinTypeOptions","JoinTypeOptionsIR","JoinValidation","JsonFormat","Label","LazySerde","LiteralValue","MaintainOrderJoin","NestedType","NonExistent","NullStrategy","NullValues","Operator","ParallelStrategy","ParquetCompression","ParquetStatistics","PolarsError","PowFunction","QuantileMethod","QuoteStyle","RankMethod","ReshapeDimension","RevMapping","RollingFnParams","SearchSortedSide","Selector","StartBy","StringFunction","StructFunction","TemporalFunction","TimeUnit","UniqueKeepStrategy","UnknownKind","WindowMapping","WindowType"],"fn":["_coalesce_full_join","_join_suffix_name","_set_check_length","abs","all","all_horizontal","any_horizontal","apply_binary","apply_multiple","apply_projection","arange","arg_sort_by","arg_where","as_struct","avg","base_utc_offset","binary_expr","call_categorical_merge_operation","cast","clip","clip_max","clip_min","coalesce","coalesce_columns","col","collect_all","cols","columns_to_projection","concat","concat_arr","concat_expr","concat_lf_diagonal","concat_lf_horizontal","concat_list","concat_str","convert_inner_type","convert_to_unsigned_index","count_ones","count_rows","count_rows_from_slice","count_zeros","create_enum_dtype","create_sorting_map","cum_count","cum_fold_exprs","cum_max","cum_min","cum_prod","cum_reduce_exprs","cum_sum","date_ranges","datetime","datetime_range","datetime_ranges","datetime_to_timestamp_ms","datetime_to_timestamp_ns","datetime_to_timestamp_us","decode_json_response","default_join_ids","deserialize","diff","dst_offset","dtype_col","dtype_cols","duration","ensure_duration_matches_dtype","ensure_is_constant_duration","ensure_matching_schema","escape_regex","escape_regex_str","expand_paths","expand_paths_hive","expanded_from_single_directory","first","floor_div_series","fmt_group_by_column","fold_exprs","format_str","get_encodings","get_glob_start_idx","get_reader_bytes","get_strftime_format","group_by_values","group_by_windows","hor_str_concat","impl_duration","impl_replace_time_zone","impl_replace_time_zone_fast","in_nanoseconds_window","index_cols","indexes_to_usizes","infer_file_schema","infer_schema","int_range","int_ranges","interpolate","interpolate_by","is_between","is_cloud_url","is_first_distinct","is_in","is_last_distinct","is_not_null","is_null","is_positive_idx_uncertain","is_positive_idx_uncertain_col","last","leading_ones","leading_zeros","len","linear_space","lit","make_categoricals_compatible","make_list_categoricals_compatible","map_binary","map_list_multiple","map_multiple","materialize_empty_df","materialize_projection","max","mean","median","merge_dtypes","min","negate","negate_bitwise","new_int_range","new_linear_space_f32","new_linear_space_f64","not","nth","overwrite_schema","prepare_cloud_plan","private_left_join_multiple_keys","quantile","reduce_exprs","remove_bom","repeat","repeat_by","replace","replace_date","replace_datetime","replace_or_default","replace_strict","replace_time_zone","resolve_homedir","split_helper","split_to_struct","str_join","strip_chars","strip_chars_end","strip_chars_start","strip_prefix","strip_suffix","sum","ternary_expr","time_ranges","trailing_ones","trailing_zeros","try_raise_keyboard_interrupt","try_set_sorted_flag","unique_counts","when","write_partitioned_dataset"],"macro":["df","polars_bail","polars_ensure","polars_err","polars_warn"],"mod":["_csv_read_internal","_internal","aggregations","arity","array","binary","buffer","byte_source","cat","chunkedarray","cloud","compression","concat_arr","datatypes","datetime","default_arrays","dt","expr","file","fill_null","fixed_size_list","float_sorted_arg_max","full","function_expr","gather","interpolate","interpolate_by","mode","nan_propagating_aggregate","null","replace","row_encode","schema_inference","search_sorted","series","sort","strings","udf","utf8","zip"],"static":["BOOLEAN_RE","EXTENSION_NAME","FLOAT_RE","FLOAT_RE_DECIMAL","INTEGER_RE","POLARS_TEMP_DIR_BASE_PATH"],"struct":["AnonymousScanArgs","AnonymousScanOptions","Arc","ArrayNameSpace","ArrowField","AsOfOptions","BatchedCsvReader","BatchedParquetReader","BinaryOffsetType","BinaryType","BooleanChunkedBuilder","BooleanType","Bounds","BoundsIter","BrotliLevel","CatIter","CategoricalChunked","CategoricalChunkedBuilder","CategoricalNameSpace","CategoricalType","ChainedThen","ChainedWhen","ChunkId","ChunkedArray","CompatLevel","CrossJoinOptions","CsvParseOptions","CsvReadOptions","CsvReader","CsvWriter","CsvWriterOptions","DataFrame","DateType","DatetimeArgs","DatetimeType","DecimalType","Dimension","Duration","DurationArgs","DurationType","DynamicGroupOptions","ExprNameNameSpace","FalseT","Field","FieldsMapper","FileMetadata","FixedSizeListType","Float32Type","Float64Type","GlobalRevMapMerger","GroupBy","GroupPositions","GroupsIdx","GroupsTypeIter","GroupsTypeParIter","GzipLevel","IEJoinOptions","InProcessQuery","Int128Type","Int16Type","Int32Type","Int64Type","Int8Type","IpcReadOptions","IpcReader","IpcReaderAsync","IpcScanOptions","IpcStreamReader","IpcStreamWriter","IpcStreamWriterOption","IpcWriter","IpcWriterOptions","JoinArgs","JoinBuilder","JoinOptions","JsonLineReader","JsonReader","JsonWriter","JsonWriterOptions","LazyCsvReader","LazyFrame","LazyGroupBy","LazyJsonLineReader","ListBinaryChunkedBuilder","ListBooleanChunkedBuilder","ListNameSpace","ListPrimitiveChunkedBuilder","ListStringChunkedBuilder","ListType","Logical","NoNull","Null","NullableIdxSize","ObjectType","OptFlags","OwnedBatchedCsvReader","OwnedObject","ParquetAsyncReader","ParquetOptions","ParquetReader","ParquetWriteOptions","ParquetWriter","PlSmallStr","PrimitiveChunkedBuilder","RankOptions","RollingCovOptions","RollingGroupOptions","RollingOptionsDynamicWindow","RollingOptionsFixedWindow","RollingQuantileParams","RollingVarParams","Scalar","ScanArgsAnonymous","ScanArgsIpc","ScanArgsParquet","SerializeOptions","Series","SortMultipleOptions","SortOptions","SpecialEq","SplitNChars","StatisticsOptions","StringCacheHolder","StringType","StrptimeOptions","StructArray","StructNameSpace","StructType","Then","TimeType","TrueT","UInt16Type","UInt32Type","UInt64Type","UInt8Type","UnionArgs","UnpivotArgsDSL","UnpivotArgsIR","UserDefinedFunction","When","Window","ZstdLevel"],"trait":["AnonymousScan","ArgAgg","ArithmeticChunked","ArrayCollectIterExt","ArrayFromIter","ArrayFromIterDtype","AsBinary","AsList","AsRefDataType","AsString","AsofJoin","AsofJoinBy","BinaryNameSpaceImpl","BinaryUdfOutputField","CategoricalMergeOperation","ChunkAgg","ChunkAggSeries","ChunkAnyValue","ChunkApply","ChunkApplyKernel","ChunkApproxNUnique","ChunkBytes","ChunkCast","ChunkCompareEq","ChunkCompareIneq","ChunkExpandAtIndex","ChunkExplode","ChunkFillNullValue","ChunkFilter","ChunkFull","ChunkFullNull","ChunkQuantile","ChunkReverse","ChunkRollApply","ChunkSet","ChunkShift","ChunkShiftFill","ChunkSort","ChunkTake","ChunkTakeUnchecked","ChunkUnique","ChunkVar","ChunkZip","ChunkedBuilder","ChunkedCollectInferIterExt","ChunkedCollectIterExt","ChunkedSet","ColumnBinaryUdf","ColumnsUdf","CrossJoin","CrossJoinFilter","DataFrameJoinOps","DataFrameOps","DateMethods","DatetimeMethods","DurationMethods","ExprEvalExtension","FromData","FromDataBinary","FromDataUtf8","FunctionOutputField","GetAnyValue","IndexToUsize","InitHashMaps","InitHashMaps2","IntoColumn","IntoGroupsType","IntoLazy","IntoListNameSpace","IntoMetadata","IntoScalar","IntoSeries","IntoVec","IsFirstDistinct","IsLastDistinct","JoinDispatch","LazyFileListReader","LhsNumOps","ListBuilderTrait","ListFromIter","ListNameSpaceExtension","ListNameSpaceImpl","Literal","LogicalType","MetaDataExt","MinMaxHorizontal","NamedFrom","NamedFromOwned","NewChunkedArray","NumOpsDispatch","NumOpsDispatchChecked","NumericNative","PolarsDataType","PolarsFloatType","PolarsIntegerType","PolarsIterator","PolarsNumericType","PolarsObject","PolarsRound","PolarsTemporalGroupby","PolarsTruncate","PolarsUpsample","QuantileAggSeries","Reinterpret","RenameAliasFn","RollingSeries","RoundSeries","SchemaExt","SchemaExtPl","SchemaNamesAndDtypes","SerReader","SerWriter","SeriesJoin","SeriesMethods","SeriesOpsTime","SeriesRank","SeriesSealed","SeriesTrait","SlicedArray","StaticArray","StringMethods","StringNameSpaceImpl","SumMeanHorizontal","TakeChunked","TakeChunkedHorPar","TemporalMethods","TimeMethods","ToDummies","UdfSchema","VarAggSeries","VecHash"],"type":["AllowedOptimizations","ArrayChunked","ArrayRef","ArrowSchema","BinaryChunked","BinaryChunkedBuilder","BinaryOffsetChunked","BooleanChunked","BorrowIdxItem","ChunkJoinOptIds","DateChunked","DatetimeChunked","DecimalChunked","DurationChunked","FieldRef","FieldsNameMapper","FileMetadataRef","FillNullLimit","Float32Chunked","Float64Chunked","GetOutput","GroupsSlice","IdxArr","IdxCa","IdxItem","IdxSize","IdxType","InnerJoinIds","Int128Chunked","Int16Chunked","Int32Chunked","Int64Chunked","Int8Chunked","LargeBinaryArray","LargeListArray","LargeStringArray","LeftJoinIds","ListChunked","ObjectChunked","OpaqueColumnUdf","PlHashMap","PlHashSet","PlIdHashMap","PlIndexMap","PlIndexSet","PlRandomState","PolarsResult","QuantileInterpolOptions","RowGroupIterColumns","Schema","SchemaRef","StringChunked","StringChunkedBuilder","StructChunked","TimeChunked","TimeZone","UInt16Chunked","UInt32Chunked","UInt64Chunked","UInt8Chunked"]};