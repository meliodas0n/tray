import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

static_files_path = f"{os.path.dirname('__filename__')}/static"
app.mount(static_files_path, StaticFiles(directory=static_files_path), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/item/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
  return templates.TemplateResponse(request=request, name="item.html", context={"id" : id})


if __name__ == "__main__":
  app.run()
