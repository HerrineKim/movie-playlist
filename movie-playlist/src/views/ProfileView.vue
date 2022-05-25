<template>
  <div>
    <nav-bar></nav-bar>
    <h1>{{ profile.username }}</h1>

    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.id">
        <router-link :to="{ name: 'article', params: { articlePk: article.id } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.like_articles" :key="article.id">
        <router-link :to="{ name: 'article', params: { articlePk: article.id } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import NavBar from "@/components/templates/NavBar.vue"
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components: {
    NavBar
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>