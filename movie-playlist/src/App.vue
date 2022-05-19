<template>
  <div id='app'>
    <nav>
      <router-link to='/'>Home</router-link> |
      <router-link to='/first'>First</router-link> |
      <router-link to='/search'>Search</router-link> |
      <router-link to='/search/:moviePk'>Movie Detail</router-link> |
      <router-link to='/hashtag'>Hashtag</router-link> |
      <router-link to='/actors'>Actors</router-link> | 
      <router-link to='/actors/:actorPk'>Actor</router-link> |
      <router-link to='/community'>Community</router-link> |
      <router-link to='/community/new'>New</router-link> | 
      <router-link to='/community/:articlePk'>Article Detail</router-link> |
      <router-link to='/community/:articlePk/edit'>Edit</router-link> | 
      <router-link to='/signup'>Signup</router-link> | 
      <router-link to='/login'>Login</router-link> |
      <router-link to='/logout'>Logout</router-link> |
      <router-link to='/profile/:username'>Profile</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
