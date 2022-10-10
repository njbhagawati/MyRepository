# Databricks notebook source
# MAGIC %scala
# MAGIC println("hello")

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC print("Hello")

# COMMAND ----------

# MAGIC %fs
# MAGIC 
# MAGIC cp dbfs:/FileStore/nayan/output.log dbfs:/FileStore/nayantest/

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/FileStore/nayantest/'))

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/FileStore/nayantest/

# COMMAND ----------

# MAGIC %fs head dbfs:/FileStore/nayan/output.log

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello DataBricks"

# COMMAND ----------

dbutils.fs.cp('dbfs:/FileStore/dmitriy_emelyanov/chil-mapping/hvac_runtime_jar_with_dependencies.jar','dbfs:/FileStore/nayantest/')

# COMMAND ----------

name= "Drimitriy"
print(f"Hello {name}")
%run ./test1 
print(f"Welcome back {full_name}")
