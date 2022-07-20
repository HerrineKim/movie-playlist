import axios from "axios"

const HOST = "http://localhost:8000/api/v1/"

export const api = axios.create({
  baseURL: HOST,
})
// https://velog.io/@subanggu/axios-interceptor-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0
// 요청 인터셉터
api.interceptors.request.use(
  function (config) {
    // 요청을 보내기 전에 수행할 일
  const token = localStorage.getItem('token')
  if (!token)
  return config
  // token이 없는 경우 config 포함
  config.headers.Authorization = `Token ${token}`
  return config
  }, function (error) {
    return Promise.reject(error)
})

export default api
