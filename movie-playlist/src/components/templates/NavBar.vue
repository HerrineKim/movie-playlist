<template>
<!-- <router-link to='/search/:moviePk'>Movie Detail</router-link> -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link :to="{ name: 'HomeView' }">Home</router-link> |
    <!-- <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button> -->
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
      <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
        <li class="nav-item active">
          <router-link to='/search'>Search</router-link>
        </li>
        <li class="nav-item">
          <router-link to='/hashtag'>Hashtag</router-link> 
        </li>
        <li class="nav-item">
          <router-link to='/actors'>Actors</router-link>
        </li>
        <li class="nav-item">
          <router-link to='/OST'>OST</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'articles' }">Community</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item">
          <router-link :to="{ name: 'signup' }">Signup</router-link>
          <router-link to='/login'>Login</router-link> |
        </li>
        <li v-if="isLoggedIn" class="nav-item">
          <router-link to='/logout'>Logout</router-link> |
          <router-link :to="{ name: 'profile', params: { username } }">
            {{ currentUser.username }}'s page
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