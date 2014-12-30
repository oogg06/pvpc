

recrear:
	cat estructura_db.txt | sqlite3 valores.db

carga:
	cat *.sql | sqlite3 valores.db

todo: 
	./descargar.py 
	./procesar_hojas.py > datos.sql;
	cat datos.sql | sqlite3 valores.db;
	echo "select * from valores;" | sqlite3 valores.db
	./crear_graficos.py;
	cp *.png /media/invitado/OSCAR/pruebas/web/content/images
 
	
fichero_sql:
	cat estructura_db.txt > fichero_datos_pvpc.sql;
	cat datos.sql >> fichero_datos_pvpc.sql
clean:
	rm Errores*;rm *.png;
	rm valores.db;
	yes | rm *.png
