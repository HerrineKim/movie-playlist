<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input type="text" id="title" v-model="newArticle.title">
    </div>
    <div>
      <label for="content">contnet: </label>
      <textarea type="text" id="content" v-model="newArticle.content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>
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