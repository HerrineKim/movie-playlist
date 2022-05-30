import axios from "axios"

const HOST = "http://localhost:8000/api/v1/"

export const api = axios.create({
  baseURL: HOST,
})

api.interceptors.request.use(function (config) {
  const token = localStorage.getItem('token')
  // token이 없는 경우는 config
  if (!token) return config
  // token이 없는 경우 config 포함
  config.headers.Authorization = `Token ${token}`
  return config
  }, function (error) {
    return Promise.reject(error)
})

export default api
