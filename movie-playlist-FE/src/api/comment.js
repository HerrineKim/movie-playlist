import api from "./api"

export default {
  create(articlePk, data) {
    return api({
      method: "post",
      url: `articles/${articlePk}/comments/`,
      data: data,
    })
  },
  update(articlePk, commentPk, data) {
    return api({
      method: "put",
      url: `articles/${articlePk}/comments/${commentPk}/`,
      data: data,
    })
  },
  delete(articlePk, commentPk) {
    return api({
      method: "delete",
      url: `articles/${articlePk}/comments/${commentPk}/`,
    })
  },
}
