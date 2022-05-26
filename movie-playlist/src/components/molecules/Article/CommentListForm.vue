<template>
  <div class="container">
    <form @submit.prevent="onSubmit" class="comment-list-form">
      <div style="float: left; padding-right: 400px">
        <label class="form-label" style="font-family:MapoGoldenPier; float: left;" for="comment">
          댓글 남기기
        </label>
      </div>
      <div >
        <input style="margin-right: 40px" class="form-control" type="text" id="comment" v-model="content" required>
      </div>
      <div class="">
        <button 
        style="float: right; font-family:GimpoGothic; margin-top: 10px"
        class="mt-3 btn btn-outline-secondary waves-effect mb-4">
          입력</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters([
      'article'
    ]),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
</style>