# In[] : Praktikum1
import shapefile
w =shapefile.Writer('soal1')
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.record("ngok","dua")
w.point(1,1)
w.point(2,2)
w.close()
# In[] : Praktikum 2
import shapefile
w = shapefile.Writer('soal2', shapeType=1)
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()

# In[] : Praktikum 3
import shapefile
w = shapefile.Writer('soal3', shapeType=1)
w.shapeType 
w.shapeType = 1
w.shapeType 
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()


# In[] : Praktikum 4
import shapefile
w = shapefile.Writer('soal4', shapefile.POINT)
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()

# In[] : Praktikum 5

import shapefile
w=shapefile.Writer('soal5')
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.close()

# In[] : Praktikum 6
import shapefile
w=shapefile.Writer('soal6',shapeType=shapefile.POLYLINE)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line([[[1,3],[5,3]]])
w.close()

# In[] : Praktikum 7
import shapefile
w=shapefile.Writer('soal7',shapeType=shapefile.POLYLINE)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line([[[1,3],[5,3],[1,2],[5,2]]])
w.close()

# In[] : Praktikum 8
import shapefile
w=shapefile.Writer('soal8',shapeType=5)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])
w.close()

# In[] : Praktikum 9
import shapefile
w=shapefile.Writer('soal9',shapeType=shapefile.POLYGON)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.record("crot","dua")
w.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
w.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])
w.close()

# In[] : Praktikum 10

print(1174002 % 8)

import shapefile
habib=shapefile.Writer('soal10', shapeType=5)
habib.field("k1","C")
habib.field("k2","C") 
habib.record("ahh","uhh") 

habib.poly([[[7,1],[12,1],[12,6],[7,6],[7,1]]])

habib.close() #penutup

#%%
