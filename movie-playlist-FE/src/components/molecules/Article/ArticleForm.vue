<template>


  <div class="container">
    <form @submit.prevent="onSubmit" class="px-5">
      <div class="" style="padding-right: 400px;">
        <label style="float: left; font-family:GimpoGothicBold00; font-size:20px;" class="form-label" for="title">제목 </label>
        <input class="form-control" type="text" id="title" v-model="newArticle.title">
      </div>
      <div class="mt-3">
        <label style="float: left; font-family:GimpoGothicBold00; font-size:20px;" class="form-label" for="content">내용 </label>
        <textarea class="form-control" type="text" id="content" v-model="newArticle.content"></textarea>
      </div>
      <button style="float: right; font-family:GimpoGothic" class="mt-3 btn btn-outline-secondary waves-effect mb-4">글쓰기</button>
    </form>
    
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'ArticleForm',
  props: {
    article: {
      type: Object,
    },
    // title: String, 
    // content: String,
    action: String,
  },
  data() {
    return {
      newArticle: {
        title: this.article.title,
        content: this.article.content
      }
    }
  },
  methods: {
    ...mapActions(['createArticle', 'updateArticle',]),
    onSubmit() {
      if (this.action === 'create') {
        const payload = this.newArticle
        this.createArticle(payload)
      } else if (this.action === 'update') {
        const payload = { articlePk: this.article.pk, ...this.newArticle}
        this.updateArticle(payload)
      }
    }
  },
  watch: {
    article: {
      handler() {
        this.newArticle = this.article
      }
    }
  }
}
</script>

<style>

</style>