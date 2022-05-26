<template>
<!-- <router-link to='/search/:moviePk'>Movie Detail</router-link> -->
  <nav class="navbar navbar-expand-lg navbar-light">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <div>
            <router-link style="color: #005aa7; font-family: 'GmarketSansMedium';" class="nav-link" :to="{ name: 'HomeView' }">
              HOME
              <img style="width:22px; height:22px" src="@/assets/images/HomeIcon.png" alt="">
            </router-link>
          </div><br>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" to='/search'>영화 |</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" to='/hashtag'>#무플리 |</router-link> 
        </li>
        <li class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" to='/actors'>인물 |</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" to='/OST'>이노래 어디 나왔더라 |</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" :to="{ name: 'articles' }">커뮤니티 ||</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" to='/login'>로그인</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" :to="{ name: 'signup' }">회원가입 </router-link>
        </li>
        <li v-if="isLoggedIn" class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" to='/logout'>로그아웃 </router-link>
        </li>
        <li v-if="isLoggedIn" class="nav-item">
          <router-link class="nav-link" style="font-family: 'GmarketSansMedium';" :to="{ name: 'profile', params: { username } }">
            마이페이지
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
@font-face {
  font-family: 'GmarketSansMedium';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
</style>