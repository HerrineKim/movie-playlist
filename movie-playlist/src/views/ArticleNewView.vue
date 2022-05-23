<template>
  <div>
    <h1>New Article</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/molecules/Article/ArticleForm.vue'

export default {
  name: 'AritcleNewView',
  components: { ArticleForm },
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
