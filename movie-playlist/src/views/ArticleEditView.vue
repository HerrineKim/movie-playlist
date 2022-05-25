<template>
  <div>
    <nav-bar></nav-bar>
    <h1>Edit Article</h1>
    <article-form :article="article" action="update"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/molecules/Article/ArticleForm.vue'
import NavBar from '@/components/templates/NavBar.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'AritcleEditView',
  components: { ArticleForm, NavBar },
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