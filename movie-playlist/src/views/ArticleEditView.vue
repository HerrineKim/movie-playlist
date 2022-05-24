<template>
  <div>
    <h1>Edit Article</h1>
    <article-form :article="article" action="update"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/molecules/Article/ArticleForm.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'AritcleEditView',
  components: { ArticleForm },
  data() {
    return {
      articlePk: '',
    }
  },
  computed: {
    ...mapGetters(['article']),
  },  
  methods: {
    ...mapActions(['fetchArticle'])
  },
  created () {
    this.articlePk = this.$route.params.articlePk
    this.fetchArticle({ articlePk: this.articlePk })
  },
}
</script>

<style>

</style>