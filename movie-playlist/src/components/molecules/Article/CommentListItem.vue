<template>
  <div class="container mt-3">
    <div class="">
      <div class="" style="text-align:left; font-family: 'GmarketSansMedium';">
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
          {{ comment.user.username }}
        </router-link>: 
        <div style="font-family: 'GmarketSansMedium';" v-if="!isEditing">{{ payload.content }}</div>

        <span>
          <div v-if="isEditing">
            <input type="text" v-model="payload.content">
            <button @click="onUpdate">Update</button> |
            <button @click="switchIsEditing">Cancle</button>
          </div>
          <div style="float:right;" v-if="currentUser.username === comment.user.username && !isEditing">
            <button class=" mt-3 btn btn-sm btn-outline-secondary waves-effect " @click="deleteComment(payload)">삭제</button>
            <button class="mt-3 mx-2 btn btn-sm btn-outline-secondary waves-effect " @click="switchIsEditing">수정</button>
          </div>
        </span>
        <br>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>

</style>