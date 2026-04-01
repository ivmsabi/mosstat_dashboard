from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

app = FastAPI(title="Mosstat API", description="API для доступа к данным Мосстата", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

@app.get("/")
def root():
    return {"message": "Mosstat API", "status": "running"}

@app.get("/api/cpi")
def get_cpi(year: Optional[int] = Query(None), month: Optional[str] = Query(None)):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT year, month, cpi FROM cpi WHERE 1=1"
    params = []
    
    if year:
        query += " AND year = %s"
        params.append(year)
    if month:
        query += " AND month = %s"
        params.append(month)
    
    query += " ORDER BY year, month LIMIT 1000"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return {"data": [{"year": r[0], "month": r[1], "cpi": r[2]} for r in rows]}

@app.get("/api/income")
def get_income(year: Optional[int] = Query(None)):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT year, indicator, value FROM income WHERE 1=1"
    params = []
    
    if year:
        query += " AND year = %s"
        params.append(str(year))
    
    query += " ORDER BY year"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return {"data": [{"year": r[0], "indicator": r[1], "value": r[2]} for r in rows]}

@app.get("/api/poverty")
def get_poverty(year: Optional[int] = Query(None)):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT year, poverty_percent FROM poverty WHERE 1=1"
    params = []
    
    if year:
        query += " AND year = %s"
        params.append(year)
    
    query += " ORDER BY year"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return {"data": [{"year": r[0], "poverty_percent": r[1]} for r in rows]}

@app.get("/api/disease")
def get_disease(year: Optional[int] = Query(None), disease_name: Optional[str] = Query(None)):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT year, disease, cases FROM disease WHERE 1=1"
    params = []
    
    if year:
        query += " AND year = %s"
        params.append(year)
    if disease_name:
        query += " AND disease = %s"
        params.append(disease_name)
    
    query += " ORDER BY year, disease LIMIT 1000"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return {"data": [{"year": r[0], "disease": r[1], "cases": r[2]} for r in rows]}

@app.get("/api/medical-staff")
def get_medical_staff(year: Optional[int] = Query(None), staff_type: Optional[str] = Query(None)):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT Годы, staff_type, count FROM medical_staff WHERE 1=1"
    params = []
    
    if year:
        query += " AND Годы = %s"
        params.append(year)
    if staff_type:
        query += " AND staff_type = %s"
        params.append(staff_type)
    
    query += " ORDER BY Годы, staff_type"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return {"data": [{"year": r[0], "staff_type": r[1], "count": r[2]} for r in rows]}

@app.get("/api/all-data")
def get_all_data():
    conn = get_db_connection()
    cur = conn.cursor()
    
    result = {}
    
    cur.execute("SELECT COUNT(*) FROM cpi")
    result['cpi_count'] = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(*) FROM income")
    result['income_count'] = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(*) FROM poverty")
    result['poverty_count'] = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(*) FROM disease")
    result['disease_count'] = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(*) FROM medical_staff")
    result['medical_staff_count'] = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
