FROM node:alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY tsconfig.json index.ts ./ 
COPY routes/ ./routes/
RUN npm run build  

FROM node:alpine

WORKDIR /app
COPY --from=builder /app/package.json /app/package-lock.json ./
RUN npm ci --only=production

COPY --from=builder /app/dist /app/dist

EXPOSE 3000

CMD ["npm", "run", "serve"]