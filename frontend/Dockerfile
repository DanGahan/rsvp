# Use the official Node.js image as a parent image
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install Angular CLI
RUN npm install -g @angular/cli@latest

# Install project dependencies
RUN npm install

# Copy the current directory contents into the container
COPY . .

# Make port 4200 available to the world outside this container
EXPOSE 4200

# Run ng serve when the container launches
CMD ["npm", "start"]
