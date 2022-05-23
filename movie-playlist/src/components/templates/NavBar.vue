<template>
  <nav>
    <ul>
      <li>
        <router-link :to="{ name: 'HomeView' }">Home</router-link> | <router-link to='/first'>First</router-link> |
      </li>
      <li>
        <router-link to='/search'>Search</router-link> | <router-link to='/search/:moviePk'>Movie Detail</router-link> | <router-link to='/hashtag'>Hashtag</router-link> |
        <router-link to='/actors'>Actors</router-link> | <router-link to='/actors/:actorPk'>Actor</router-link> |
        <router-link to='/OST'>OST</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'articles' }">Community</router-link> |
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link to='/logout'>Logout</router-link> |
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link to='/login'>Login</router-link> |
      </li>
    </ul>
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