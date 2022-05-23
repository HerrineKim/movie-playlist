import router from "@/router"
import article from "@/api/article"
import comment from "@/api/comment"

export default {
  state: {
    articles: [],
    article: { title: "", content: "" },
  },

  getters: {
    articles: (state) => state.articles,
    article: (state) => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser?.username
    },
  },

  mutations: {
    SET_ARTICLES: (state, articles) => (state.articles = articles),
    SET_ARTICLE: (state, article) => (state.article = article),
    SET_ARTICLE_COMMENTS: (state, comments) =>
      (state.article.comments = comments),
  },

  actions: {
    fetchArticles({ commit }) {
      article
        .all()
        .then((res) => {
          commit("SET_ARTICLES", res.data);
        })
        .catch((err) => console.error(err.response));
    },

    fetchArticle({ commit }, { articlePk }) {
      article
        .detail(articlePk)
        .then((res) => {
          commit("SET_ARTICLE", res.data)
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },

    createArticle({ commit, getters }, { title, content }) {
      const body = { title, content }
      article
        .create(body)
        .then((res) => {
          commit("SET_ARTICLE", res.data)
          router.push({
            name: "article",
            params: { articlePk: getters.article.pk },
          });
        })
        .catch((err) => console.error(err.response))
    },

    updateArticle({ commit, getters }, { title, content, articlePk }) {
      const body = { title, content }
      article
        .update(articlePk, body)
        .then((res) => {
          commit("SET_ARTICLE", res.data)
          router.push({
            name: "article",
            params: { articlePk: getters.article.pk },
          });
        })
        .catch((err) => console.error(err.response))
    },

    deleteArticle({ commit }, { articlePk }) {
      article
        .delete(articlePk)
        .then(() => {
          commit("SET_ARTICLE", {});
          router.push({ name: "articles" });
        })
        .catch((err) => console.error(err.response))
    },

    likeArticle({ commit }, { articlePk }) {
      article
        .like(articlePk)
        .then((res) => {
          commit("SET_ARTICLE", res.data);
        })
        .catch((err) => console.error(err.response))
    },

    createComment({ commit }, { articlePk, content }) {
      const body = { content }
      comment
        .create(articlePk, body)
        .then((res) => {
          commit("SET_ARTICLE_COMMENTS", res.data)
        })
        .catch((err) => console.error(err.response))
    },

    updateComment({ commit }, { articlePk, commentPk, content }) {
      const body = { content }
      comment
        .update(articlePk, commentPk, body)
        .then((res) => {
          commit("SET_ARTICLE_COMMENTS", res.data)
        })
        .catch((err) => console.error(err.response))
    },

    deleteComment({ commit }, { articlePk, commentPk }) {
      comment
        .delete(articlePk, commentPk)
        .then((res) => {
          commit("SET_ARTICLE_COMMENTS", res.data)
        })
        .catch((err) => console.error(err.response))
    },
  },
}
