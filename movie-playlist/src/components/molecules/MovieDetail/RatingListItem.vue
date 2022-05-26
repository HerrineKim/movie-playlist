<template>
  <div class="container" 
  style="text-align:left;">
    <p style="text-decoration:none;font-family:GmarketSansMedium;">
      <router-link :to="{ name: 'profile', params: { username: rating.user.username} }">
          {{ rating.user.username }}
      </router-link> 님은
    </p>
    <span v-if="!isEditing"
    style="font-family:GmarketSansMedium;"
    >이 영화를 {{ payload.rate }} 점으로 평가하셨습니다</span>

    <span v-if="isEditing">
      <input class="form-control" style="padding-right:100px;" type="text" v-model="payload.rate">
      <button class="mt-3 mx-1 btn btn-sm btn-outline-secondary waves-effect" @click="onUpdate">업데이트</button>
      <button class="mt-3 mx-1 btn btn-sm btn-outline-secondary waves-effect" @click="switchIsEditing">삭제</button>
    </span>
    <br>
    <span v-if="currentUser.username === rating.user.username && !isEditing">
      <button class="mt-3 btn btn-sm btn-outline-secondary waves-effect" @click="switchIsEditing">
        수정
      </button>
      <button class="mt-3 mx-1 btn btn-sm btn-outline-secondary waves-effect" @click="deleteRating(payload)">
        삭제
      </button>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingListItem',
  props: { rating: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.rating.movie,
        ratingPk: this.rating.id,
        rate: this.rating.rate
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  methods: {
    ...mapActions(['updateRating', 'deleteRating']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateRating(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style>

</style>