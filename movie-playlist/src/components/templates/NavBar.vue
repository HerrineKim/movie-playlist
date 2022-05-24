<template>
<!-- <router-link to='/search/:moviePk'>Movie Detail</router-link> -->
  <nav class="navbar navbar-expand-lg navbar-light">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'HomeView' }">무플리 홈</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to='/search'>영화</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to='/hashtag'>#무플리</router-link> 
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to='/actors'>인물</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to='/OST'>이거 어디서 나온 노래지?</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'articles' }">커뮤니티</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item">
          <router-link class="nav-link" to='/login'>로그인</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item">
          <router-link class="nav-link" :to="{ name: 'signup' }">회원가입</router-link>
        </li>
        <li v-if="isLoggedIn" class="nav-item">
          <router-link class="nav-link" to='/logout'>로그아웃</router-link>
        </li>
        <li v-if="isLoggedIn" class="nav-item">
          <router-link class="nav-link" :to="{ name: 'profile', params: { username } }">
            내 정보
          </router-link>
        </li>
      </ul>
    </div>
  </nav> 
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    }
  },
}
</script>

<style>

</style>