# Use formal Node LTS image as the base stage
FROM node:20-alpine AS base

# Install core dependencies needed by some node-gyp operations
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Copy dependency descriptors to cache installation steps
COPY package.json package-lock.json* ./

# Install packages with strict compliance to package-lock
RUN npm ci

# Copy all engineering source code files
COPY . .

# Disable Next.js telemetry collection during build time
ENV NEXT_TELEMETRY_DISABLED=1

# Expose Next.js default port
EXPOSE 3000

# Run developmental Next.js platform server (Adjustable to multi-stage production build later)
CMD ["npm", "run", "dev"]