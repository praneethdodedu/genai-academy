# Optional Dockerfile — only needed for a self-hosted VPS deployment (see
# docker-compose.yml at the project root and DEPLOYMENT.md, Option C).
# Not needed if you deploy the frontend to Vercel/Netlify (Option A) — they
# build directly from the frontend/ folder.

# --- Build stage ---
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Pass the backend URL at build time, e.g.:
#   docker build --build-arg VITE_API_URL=https://api.yourdomain.com .
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

# --- Serve stage ---
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
