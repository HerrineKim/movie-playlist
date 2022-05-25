<template>
  <li>
    <router-link :to="{ name: 'profile', params: { username: rating.user.username} }">
      {{ rating.user.username }}
    </router-link>
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === rating.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteRating(payload)">Delete</button>
    </span>
  </li>
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