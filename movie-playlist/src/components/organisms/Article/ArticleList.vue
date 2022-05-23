<template>
  <div>
    <ul>
      <li v-for="article in articles" :key="article.pk">
        <!-- User -->
        <router-link :to="{ name: 'profile', params: { username: article.user.username} }">
          {{ article.user.username }}
        </router-link>

        => 
        
        <!-- Title -->
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>

        <!-- Info -->
        ({{ article.comment_count }}) | +{{ article.like_count }}
      </li>
    </ul>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'



export default {
  name: 'ArticleList',
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  },
}
</script>

<style>

</style>