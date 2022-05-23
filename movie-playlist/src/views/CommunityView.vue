<template>
  <div class="community">
    <h2>커뮤니티 게시판 메인 화면</h2>
    <article-list></article-list>
    <com-create-button></com-create-button>
    <div v-if="isLoggedIn">
      <router-link :to="{ name: 'articleNew' }">
        <button>New</button>
      </router-link>
  </div>
  </div>
</template>

<script>
import ArticleList from '@/components/organisms/Article/ArticleList.vue'
import ComCreateButton from '@/components/molecules/Community/ComCreateButton.vue'

export default {
  name: 'CommunityView',
  components: { 
    ArticleList,
    ComCreateButton,
  }
}
</script>

<style>

</style>