<template>
  <div class="container" style="text-align:left">
    <p>
      <router-link :to="{ name: 'profile', params: { username: rating.user.username} }">
        {{ rating.user.username }}
      </router-link>
      
      <span v-if="!isEditing">{{ payload.rate }}</span>

      <span v-if="isEditing">
        <input type="text" v-model="payload.content">
        <button @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancle</button>
      </span>
      <br>
      <span v-if="currentUser.username === rating.user.username && !isEditing">
        <button class="mt-3 btn btn-sm btn-outline-secondary waves-effect" @click="switchIsEditing">Edit</button>
        <button class="mt-3 mx-1 btn btn-sm btn-outline-secondary waves-effect" @click="deleteRating(payload)">Delete</button>
      </span>
    </p>
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