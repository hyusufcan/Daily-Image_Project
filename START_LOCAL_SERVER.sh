#!/bin/bash
# The Daily Antiquarian - Quick Start Shell Script
# Linux/macOS için

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          🏛️  The Daily Antiquarian - Dev Server              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if requirements are installed
if ! python -m pip show requests &> /dev/null; then
    echo "⚠️  Installing dependencies..."
    python -m pip install -r requirements.txt
else
    echo "✅ Dependencies already installed"
fi

echo ""
echo "🚀 Starting development server..."
echo ""
echo "📍 Website:  http://localhost:8000/public/"
echo "📝 Files:    $(pwd)"
echo ""
echo "Press CTRL+C to stop the server."
echo ""

python -m http.server 8000 --directory public

