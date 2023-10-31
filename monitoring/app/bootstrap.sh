echo " - Monitoring container started ..."
echo " - Application: $APPLICATION"

export ROOT_FOLDER=$(pwd)
echo " - ROOT_FOLDER:    "$ROOT_FOLDER

if [ $APPLICATION == "start-server" ]; then
  uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port $ServerPort
fi