@echo off
echo ========================================
echo   Starting GRA - Generative Resilience Agent
echo ========================================
echo.

echo [1/2] Starting Backend Server...
start "GRA Backend" cmd /k "cd backend && python main.py"
timeout /t 3 /nobreak > nul

echo [2/2] Starting Frontend Server...
start "GRA Frontend" cmd /k "cd frontend && python -m http.server 3000"
timeout /t 2 /nobreak > nul

echo.
echo ========================================
echo   GRA is now running!
echo ========================================
echo.
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8001
echo.
echo   Opening browser...
echo ========================================

timeout /t 2 /nobreak > nul
start http://localhost:3000

echo.
echo Press any key to stop all servers...
pause > nul

echo.
echo Stopping servers...
taskkill /FI "WINDOWTITLE eq GRA Backend*" /F > nul 2>&1
taskkill /FI "WINDOWTITLE eq GRA Frontend*" /F > nul 2>&1

echo.
echo All servers stopped.
echo.
pause