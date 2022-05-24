export default {
  name: "HashtagMovies",
  data(){
    return{
      checkedGenres:[],
      checkedCasetags: [],
      checkedMoodtags:[],
      // genre_movies: { id: "", movies: [] },
      // moodtag_movies: { id: "", movies: [] },
      // casetag_movies: { id: "", movies: [] },
    }
  },
  computed: {
    // genrePk: function() {
    //   return this.checkedGenres[0]
    // },
    // moodtagPk: function() {
    //   return this.checkedCasetags[0]
    // },
    // casetagPk: function() {
    //   return this.checkedMoodtags[0]
    // },
    ...mapGetters(['moodtag_movies', 'casetag_movies', 'genre_movies'])
  },
  methods: {
    ...mapActions(['fetchGenreMovies', 'fetchMoodtagMovies', 'fetchCasetagMovies'])
    // fetchGenreMovies: function() {
    //   axios({
    //     method: "GET",
    //     url: `http://127.0.0.1:8000/api/v1/movies/genre/${this.genrePk}/`,
    //   }).then((res) => {
    //       this.genre_movies = res.data
    //       console.log(res.data)
    //   }).catch((err) => {
    //     if (err.response.status === 404) {
    //       router.push({ name: "NotFound404" });
    //     }
    //   })
    // },
  },
  created() {
    this.fetchGenreMovies({ genrePk: '35' })
    this.fetchMoodtagMovies({ moodtagPk: '2' })
    this.fetchCasetagMovies({ casetagPk: '2' })
  }
}
</script>

<style>

</style>