<template>
  <div class="container">
    <nav-bar></nav-bar>
    <div class="container mt-5">
      <h1 style="font-family:MapoGoldenPier">
        새 글
      </h1>
      <article-form class="mt-5" :article="article" action="create"></article-form>
    </div>
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
