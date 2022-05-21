<template>
  <div>
    <nav>
      <ul>
        <li>
          <router-link :to="{ name: 'HomeView' }">Home</router-link>
        </li>
        <li>
          <router-link to='/first'>First</router-link> |
        </li>
        <li>
          <router-link to='/search'>Search</router-link> |
        </li>
        <li>
          <router-link to='/search/:moviePk'>Movie Detail</router-link> |
        </li>
        <li>
          <router-link to='/hashtag'>Hashtag</router-link> |
        </li>
        <li>
          <router-link to='/actors'>Actors</router-link> | <router-link to='/actors/:actorPk'>Actor</router-link> |

        </li>
        <li>
          <router-link to='/community'>Community</router-link> | <router-link to='/community/new'>New</router-link> | 
          <router-link to='/community/:articlePk'>Article Detail</router-link> | <router-link to='/community/:articlePk/edit'>Edit</router-link> | 
        </li>
        <li v-if="isLoggedIn">
          <router-link to='/logout'>Logout</router-link> |
        </li>
        <li>
          <router-link v-if="!isLoggedIn" to='{ name: signup }'>Signup</router-link> |
          <router-link v-if="!isLoggedIn" to='/login'>Login</router-link> |
          <router-link v-if="isLoggedIn" to='/profile/:username'>{{ currentUser.username }}'s page</router-link>
        </li>
      </ul>
    </nav>
  </div>
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