use super::*;
use crate::chunked_array::comparison::*;
#[cfg(feature = "algorithm_group_by")]
use crate::frame::group_by::*;
use crate::prelude::row_encode::_get_rows_encoded_ca_unordered;
use crate::prelude::*;

impl private::PrivateSeries for SeriesWrap<ListChunked> {
    fn compute_len(&mut self) {
        self.0.compute_len()
    }
    fn _field(&self) -> Cow<'_, Field> {
        Cow::Borrowed(self.0.ref_field())
    }
    fn _dtype(&self) -> &DataType {
        self.0.ref_field().dtype()
    }
    fn _get_flags(&self) -> StatisticsFlags {
        self.0.get_flags()
    }
    fn _set_flags(&mut self, flags: StatisticsFlags) {
        self.0.set_flags(flags)
    }

    unsafe fn equal_element(&self, idx_self: usize, idx_other: usize, other: &Series) -> bool {
        self.0.equal_element(idx_self, idx_other, other)
    }

    fn vec_hash(
        &self,
        build_hasher: PlSeedableRandomStateQuality,
        buf: &mut Vec<u64>,
    ) -> PolarsResult<()> {
        _get_rows_encoded_ca_unordered(PlSmallStr::EMPTY, &[self.0.clone().into_column()])?
            .vec_hash(build_hasher, buf)
    }

    fn vec_hash_combine(
        &self,
        build_hasher: PlSeedableRandomStateQuality,
        hashes: &mut [u64],
    ) -> PolarsResult<()> {
        _get_rows_encoded_ca_unordered(PlSmallStr::EMPTY, &[self.0.clone().into_column()])?
            .vec_hash_combine(build_hasher, hashes)
    }

    #[cfg(feature = "zip_with")]
    fn zip_with_same_type(&self, mask: &BooleanChunked, other: &Series) -> PolarsResult<Series> {
        ChunkZip::zip_with(&self.0, mask, other.as_ref().as_ref()).map(|ca| ca.into_series())
    }

    #[cfg(feature = "algorithm_group_by")]
    unsafe fn agg_list(&self, groups: &GroupsType) -> Series {
        self.0.agg_list(groups)
    }

    #[cfg(feature = "algorithm_group_by")]
    fn group_tuples(&self, multithreaded: bool, sorted: bool) -> PolarsResult<GroupsType> {
        IntoGroupsType::group_tuples(&self.0, multithreaded, sorted)
    }

    fn into_total_eq_inner<'a>(&'a self) -> Box<dyn TotalEqInner + 'a> {
        (&self.0).into_total_eq_inner()
    }
    fn into_total_ord_inner<'a>(&'a self) -> Box<dyn TotalOrdInner + 'a> {
        invalid_operation_panic!(into_total_ord_inner, self)
    }

    fn add_to(&self, rhs: &Series) -> PolarsResult<Series> {
        self.0.add_to(rhs)
    }

    fn subtract(&self, rhs: &Series) -> PolarsResult<Series> {
        self.0.subtract(rhs)
    }

    fn multiply(&self, rhs: &Series) -> PolarsResult<Series> {
        self.0.multiply(rhs)
    }
    fn divide(&self, rhs: &Series) -> PolarsResult<Series> {
        self.0.divide(rhs)
    }
    fn remainder(&self, rhs: &Series) -> PolarsResult<Series> {
        self.0.remainder(rhs)
    }
}

impl SeriesTrait for SeriesWrap<ListChunked> {
    fn rename(&mut self, name: PlSmallStr) {
        self.0.rename(name);
    }

    fn chunk_lengths(&self) -> ChunkLenIter<'_> {
        self.0.chunk_lengths()
    }
    fn name(&self) -> &PlSmallStr {
        self.0.name()
    }

    fn chunks(&self) -> &Vec<ArrayRef> {
        self.0.chunks()
    }
    unsafe fn chunks_mut(&mut self) -> &mut Vec<ArrayRef> {
        self.0.chunks_mut()
    }
    fn shrink_to_fit(&mut self) {
        self.0.shrink_to_fit()
    }

    fn sum_reduce(&self) -> PolarsResult<Scalar> {
        polars_bail!(
            op = "`sum`",
            self.dtype(),
            hint = "you may mean to call `concat_list`"
        );
    }

    fn arg_sort(&self, options: SortOptions) -> IdxCa {
        self.0.arg_sort(options)
    }

    fn sort_with(&self, options: SortOptions) -> PolarsResult<Series> {
        Ok(self.0.sort_with(options).into_series())
    }

    fn slice(&self, offset: i64, length: usize) -> Series {
        self.0.slice(offset, length).into_series()
    }

    fn split_at(&self, offset: i64) -> (Series, Series) {
        let (a, b) = self.0.split_at(offset);
        (a.into_series(), b.into_series())
    }

    fn append(&mut self, other: &Series) -> PolarsResult<()> {
        polars_ensure!(self.0.dtype() == other.dtype(), append);
        self.0.append(other.as_ref().as_ref())
    }
    fn append_owned(&mut self, other: Series) -> PolarsResult<()> {
        polars_ensure!(self.0.dtype() == other.dtype(), append);
        self.0.append_owned(other.take_inner())
    }

    fn extend(&mut self, other: &Series) -> PolarsResult<()> {
        polars_ensure!(self.0.dtype() == other.dtype(), extend);
        self.0.extend(other.as_ref().as_ref())
    }

    fn filter(&self, filter: &BooleanChunked) -> PolarsResult<Series> {
        ChunkFilter::filter(&self.0, filter).map(|ca| ca.into_series())
    }

    fn take(&self, indices: &IdxCa) -> PolarsResult<Series> {
        Ok(self.0.take(indices)?.into_series())
    }

    unsafe fn take_unchecked(&self, indices: &IdxCa) -> Series {
        self.0.take_unchecked(indices).into_series()
    }

    fn take_slice(&self, indices: &[IdxSize]) -> PolarsResult<Series> {
        Ok(self.0.take(indices)?.into_series())
    }

    unsafe fn take_slice_unchecked(&self, indices: &[IdxSize]) -> Series {
        self.0.take_unchecked(indices).into_series()
    }

    fn len(&self) -> usize {
        self.0.len()
    }

    fn rechunk(&self) -> Series {
        self.0.rechunk().into_owned().into_series()
    }

    fn new_from_index(&self, index: usize, length: usize) -> Series {
        ChunkExpandAtIndex::new_from_index(&self.0, index, length).into_series()
    }

    fn trim_lists_to_normalized_offsets(&self) -> Option<Series> {
        self.0
            .trim_lists_to_normalized_offsets()
            .map(IntoSeries::into_series)
    }

    fn propagate_nulls(&self) -> Option<Series> {
        self.0.propagate_nulls().map(IntoSeries::into_series)
    }

    fn cast(&self, dtype: &DataType, cast_options: CastOptions) -> PolarsResult<Series> {
        self.0.cast_with_options(dtype, cast_options)
    }

    #[inline]
    unsafe fn get_unchecked(&self, index: usize) -> AnyValue<'_> {
        self.0.get_any_value_unchecked(index)
    }

    fn null_count(&self) -> usize {
        self.0.null_count()
    }

    fn has_nulls(&self) -> bool {
        self.0.has_nulls()
    }

    #[cfg(feature = "algorithm_group_by")]
    fn unique(&self) -> PolarsResult<Series> {
        if !self.inner_dtype().is_primitive_numeric() {
            polars_bail!(opq = unique, self.dtype());
        }
        // this can be called in aggregation, so this fast path can be worth a lot
        if self.len() < 2 {
            return Ok(self.0.clone().into_series());
        }
        let main_thread = POOL.current_thread_index().is_none();
        let groups = self.group_tuples(main_thread, false);
        // SAFETY:
        // groups are in bounds
        Ok(unsafe { self.0.clone().into_series().agg_first(&groups?) })
    }

    #[cfg(feature = "algorithm_group_by")]
    fn n_unique(&self) -> PolarsResult<usize> {
        // this can be called in aggregation, so this fast path can be worth a lot
        match self.len() {
            0 => Ok(0),
            1 => Ok(1),
            _ => {
                let main_thread = POOL.current_thread_index().is_none();
                let groups = self.group_tuples(main_thread, false)?;
                Ok(groups.len())
            },
        }
    }

    #[cfg(feature = "algorithm_group_by")]
    fn arg_unique(&self) -> PolarsResult<IdxCa> {
        if !self.inner_dtype().is_primitive_numeric() {
            polars_bail!(opq = arg_unique, self.dtype());
        }
        // this can be called in aggregation, so this fast path can be worth a lot
        if self.len() == 1 {
            return Ok(IdxCa::new_vec(self.name().clone(), vec![0 as IdxSize]));
        }
        let main_thread = POOL.current_thread_index().is_none();
        // arg_unique requires a stable order
        let groups = self.group_tuples(main_thread, true)?;
        let first = groups.take_group_firsts();
        Ok(IdxCa::from_vec(self.name().clone(), first))
    }

    fn is_null(&self) -> BooleanChunked {
        self.0.is_null()
    }

    fn is_not_null(&self) -> BooleanChunked {
        self.0.is_not_null()
    }

    fn reverse(&self) -> Series {
        ChunkReverse::reverse(&self.0).into_series()
    }

    fn as_single_ptr(&mut self) -> PolarsResult<usize> {
        self.0.as_single_ptr()
    }

    fn shift(&self, periods: i64) -> Series {
        ChunkShift::shift(&self.0, periods).into_series()
    }

    fn clone_inner(&self) -> Arc<dyn SeriesTrait> {
        Arc::new(SeriesWrap(Clone::clone(&self.0)))
    }

    fn find_validity_mismatch(&self, other: &Series, idxs: &mut Vec<IdxSize>) {
        self.0.find_validity_mismatch(other, idxs)
    }

    fn as_any(&self) -> &dyn Any {
        &self.0
    }

    fn as_any_mut(&mut self) -> &mut dyn Any {
        &mut self.0
    }

    fn as_phys_any(&self) -> &dyn Any {
        &self.0
    }

    fn as_arc_any(self: Arc<Self>) -> Arc<dyn Any + Send + Sync> {
        self as _
    }
}
