<template>
  <div>
    <div>
      <rating-list-item
      v-for="rating in ratings"
      :rating="rating"
      :key="rating.pk"
      ></rating-list-item>
    </div>
    <div class="my-3" style="text-align: right;">
      <rating-list-form></rating-list-form>
    </div>
  </div>
</template>

<script>
import RatingListForm from '@/components/molecules/MovieDetail/RatingListForm.vue'
import RatingListItem from '@/components/molecules/MovieDetail/RatingListItem.vue'
export default {
  components: { RatingListForm, RatingListItem },
  props: { ratings: Array },
}
</script>

<style>

</style>