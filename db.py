import sqlite3

# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator.db")


# creating cursor in the data base
c=conn.cursor()
import sqlite3

# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator.db")


# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE User_Data(
            USERNAME TEXT
            NTID VARCHAR
            ACCESS_RIGHT VARCHAR
            ACCESS_RIGHT_DATE_LIMITATION DATE
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
import sqlite3

# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE Generic_Information(
            PART_NAME TEXT
            DATE DATE
            CURRENCY TEXT
            SUPPLIER_NAME TEXT
            LOCATION TEXT
            SHIFT_MODE INT
            PRODUTION_VOLUME INT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE MATERIAL(
            MATERIAL_NAME TEXT
            DENSITY FLOAT
            WIDTH FLOAT
            HEIGHT FLOAT
            FINISHED_PART_VOLUME FLOAT
            FINISHED_PART_WEIGHT FLOAT
            NO_OF_PARTS INT
            SUPPORT_MATERIAL TEXT
            WEIGHT_OF_SUPPORT_MATERIAL FLOAT
            UNUSED_MATERIAL FLOAT
            REUSABILITY_OF_UNUSED_MATERIAL FLOAT
            MATERIAL_LOSSES FLOAT
            MATERIAL_LOSSES_IN_GRAMS FLOAT
            MATERIAL_PRICE FLOAT
            MATERIAL_COST FLOAT
            MATERIAL_OVERHEAD FLOAT
            INTEREST_ON_MATERIAL_STOCK FLOAT
            MATERIAL_SCRAP_DUE_TO_PROCESS_SCRAP FLOAT
            TOTAL_MATERIAL_COST FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE PROCESS_COST(
            MACHINE_HOURLY_RATE FLOAT
            MACHINE_SETUP_TIME FLOAT
            NUMBER_OF_PARTS FLOAT
            LASER_DIAMETER FLOAT
            NUMBER_OF_LASER_HEADS FLOAT
            PART_VOLUME FLOAT
            HATCH_SPACING INT
            SCAN_SPEED TEXT
            LAYER_THICKNESS FLOAT
            SURFACE_AREA FLOAT
            RECOATING_TIME FLOAT
            BUILDING_TIME FLOAT
            TOTAL_CYCLE_TIME FLOAT
            MACHINE_COST FLOAT
            LABOUR_COST FLOAT
            OVERHEAD_COST FLOAT
            COST_WITH_OVERHEADS FLOAT
            SCRAP_RATE FLOAT
            TOTAL_COST_INCLUDING_SCRAP_AND_OVERHEADS FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE POWDER_REMOVAL_PROCESS(
            TOTAL_TIME_FOR_POWDER_REMOVAL FLOAT
            MC_HRLY_RATE FLOAT
            PROCESS_COST_PER_PART FLOAT
            LABOUR_COST_PER_PART FLOAT
            OVERHEADS FLOAT
            TOTAL_COST_PER_PART FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE WIRE_EDM(
            NUMBER_OF_PARTS FLOAT
            LOADING_AND_UNLOADING_TIME FLOAT
            CUTTING_TIME FLOAT
            TOTAL_CYCLE_TIME FLOAT
            MACHNE_NAME TEXT
            MC_HRLY_RATE FLOAT
            PROCESS_COST_PER_PART FLOAT
            LABOUR_COST_PER_PART FLOAT
            OVERHEADS FLOAT
            TOTAL_COST_PER_PART FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE HEAT_TREATMENT(
            NUMBER_OF_PARTS_LOADED FLOAT
            LOADING_AND_UNLOADING_TIME FLOAT
            FURNACE_HOLDING_TIME FLOAT
            TOTAL_CYCLE_TIME FLOAT
            MACHNE_NAME TEXT
            MC_HRLY_RATE FLOAT
            PROCESS_COST_PER_PART FLOAT
            LABOUR_COST_PER_PART FLOAT
            OVERHEADS FLOAT
            TOTAL_COST_PER_PART FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE SHOT_PEENING(
            NUMBER_OF_PARTS_LOADED FLOAT
            LOADING_AND_UNLOADING_TIME FLOAT
            CYCLE_TIME FLOAT
            TOTAL_CYCLE_TIME FLOAT
            MACHNE_NAME TEXT
            MC_HRLY_RATE FLOAT
            PROCESS_COST_PER_PART FLOAT
            LABOUR_COST_PER_PART FLOAT
            OVERHEADS FLOAT
            TOTAL_COST_PER_PART FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE OVEREADS(
            TOTAL_COST_BEFORE_OVERHEADS FLOAT
            SGnA_PERCENTAGE FLOAT
            INTEREST_ON_FINISHED_PRODUCT_STOCK_PERCENTAGE FLOAT
            INTEREST_ON_FINISHED_STOCK FLOAT
            PROFIT_PERCENTAGE FLOAT
            PROFIT FLOAT
            INTEREST_FOR_TERMS_OF_PAYMENT_PERCENTAGE FLOAT
            INTEREST_FOR_TERMS_OF_PAYMENT FLOAT
            TOTAL_OVERHEAD_COST FLOAT
            TOTAL_COST_AFTER_OVERHEAD FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
# Create a data base in the folder
sqlite3.connect("3d Printing Calculator.db")

# Connecting to database
conn=sqlite3.connect("3d Printing Calculator")

# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE CALCULATION_SUMMARY(
            MATERIAL_COST FLOAT
            MANUFACTURING_COST FLOAT
            OVERHEAD FLOAT
            TOTAL_COST_PER_PART FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
import sqlite3

# Create a data base in the folder
sqlite3.connect("MATERIAL.db")

# Connecting to database
conn=sqlite3.connect("MATERIAL")


# creating cursor in the data base
c=conn.cursor()

#creating a table ---> CRUD Create Read Update Delete Search
c.execute("""
            CREATE TABLE MATERIAL(
            MATERIAL_NAME TEXT
            DENSITY FLOAT
            WIDTH FLOAT
            HEIGHT FLOAT
            FINISHED_PART_VOLUME FLOAT
            FINISHED_PART_WEIGHT FLOAT
            NO_OF_PARTS INT
            SUPPORT_MATERIAL TEXT
            WEIGHT_OF_SUPPORT_MATERIAL FLOAT
            UNUSED_MATERIAL FLOAT
            REUSABILITY_OF_UNUSED_MATERIAL FLOAT
            MATERIAL_LOSSES FLOAT
            MATERIAL_LOSSES_IN_GRAMS FLOAT
            MATERIAL_PRICE FLOAT
            MATERIAL_COST FLOAT
            MATERIAL_OVERHEAD FLOAT
            INTEREST_ON_MATERIAL_STOCK FLOAT
            MATERIAL_SCRAP_DUE_TO_PROCESS_SCRAP FLOAT
            TOTAL_MATERIAL_COST FLOAT
            )""")

# request for the excusion
conn.commit()

# close the connection
conn.close()
