import axios from 'axios';
import { baseURL, timeout } from './config.ts';


class Request {
    constructor(baseURL, timeout) {
        this.instance = axios.create({
            baseURL,
            timeout,
        });

        this.instance.interceptors.request.use(
            config => {

                if (sessionStorage.getItem('token')) {
                    const token = sessionStorage.getItem('token')
                    config.headers['Authorization'] = "Bearer " + token;
                }
                else {
                    config.headers['Authorization'] = "Bearer " ;
                }
                return config;
            },
            err => {
                return Promise.reject(err);
            }
        );

        this.instance.interceptors.response.use(
            res => {
                return res.data;
            },
            err => {
                return err;
            }
        );
    }

    request(config) {
        return new Promise((resolve, reject) => {
            this.instance
                .request(config)
                .then(res => {
                    resolve(res);
                })
                .catch(err => {
                    reject(err);
                });
        });
    }

    get(config) {
        return this.request({ ...config, method: 'get' });
    }

    post(config) {
        return this.request({ ...config, method: 'post' });
    }
}
export default new Request(baseURL, timeout);
