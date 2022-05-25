<template>
  <div>
    <nav-bar></nav-bar>
    <h1>New Article</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import ArticleForm from '@/components/molecules/Article/ArticleForm.vue'

export default {
  name: 'AritcleNewView',
  components: { ArticleForm, NavBar },
  data() {
    return {
      article: {
        pk: null,
        title: '',
        content: ''
      }
    }
  },
  
}
</script>

<style>

</style>
