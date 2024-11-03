import axios from 'axios';

export const useAPI = () => {
    const api = axios.create({
        baseURL: 'http://127.0.0.1:3000',  // Backend API base URL
        headers: {
            'Content-Type': 'application/json',
        },
    });

    return api;
};
