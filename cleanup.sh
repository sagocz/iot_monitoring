#!/bin/bash
echo "🧹 Cleaning up containers and network..."
docker-compose down --volumes --remove-orphans