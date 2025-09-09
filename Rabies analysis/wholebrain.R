#R version 3.6.1
quartz<-function(width,height){windows(width, height)}
setwd("D:/2020 RV projection/wholebrain/RV SC no in situ/5432")
setwd("C:/SKS_Drive/2020 RV projection/Wholebrain/RV SC VGLUT2")
folder<-'D:/2020 RV projection/wholebrain/RV SC no in situ/5432/slide 4 section 2_2_1'
library(wholebrain)
flat.field.correction(folder)
FFC_folder<-'D:/2020 RV projection/wholebrain/RV SC no in situ/5432/FFC_slide 4 section 2_2_1'
stitch(FFC_folder) #, rotate = 90
FFC_filename<-'C:/SKS_Drive/2020 RV projection/Wholebrain/RV SC VGLUT2/stitched_FFC_641_slide_11_section_2_1.tif'
seg$filter$threshold.range <- c(32542, 65536)
seg$filter$alim <- c(12,120)
seg$filter$blur <- 3
seg$filter$resize <- .04
#imshow(FFC_filename)
seg<-segment(FFC_filename, filter = seg$filter) #, filter = seg$filter #use seg$filter$threshold.range to set the intensity range, form like <- c(min, max)
#adjust parameters and then press Esc
quartz()
regi<-registration(FFC_filename, coordinate = -3.85, filter=seg$filter)
#correct manually, right first, then left, one point by one
regi<-add.corrpoints(regi, 1)
#or regi<-add.corrpoints(regi) when done just right click anywhere
#rerun registration
regi<-registration(FFC_filename, coordinate = -3.85, filter=seg$filter, correspondance = regi)
#adjust corrpoints
regi<-change.corrpoints(regi, c(36, 38))
regi<-change.corrpoints(regi, 1:17)
regi<-change.corrpoints(regi, 18:32)
regi<-change.corrpoints(regi, 1)
regi<-change.corrpoints(regi, c(15,16))
#be careful!
regi<-remove.corrpoints(regi, 38)

dataset<-inspect.registration(regi, seg, forward.warps = TRUE)
save(seg, regi, dataset, file = '641_11_2.Rdata')
write.csv(dataset, file = "641_11_2_regi.csv")
#remove unassigned cells:
#dataset<-dataset[!dataset$id==0,]
bargraph(dataset)
quartz.save(file='stitched_FFC_595-11 slide 1 section_0_1.pdf', type='pdf')

table(dataset$acronym)
table(dataset$acronym, dataset$right.hemisphere)

dataset<-inspect.registration(regi, seg)
#set pixel resolution in microns
pixel.resolution<-0.64
#name of channel imaged
protein <- "EGFP"
#make a web map output of your result
makewebmap(FFC_filename, 
           seg$filter, 
           registration = regi, 
           dataset = dataset, 
           scale = pixel.resolution, 
           fluorophore = protein
)

###schematic
schematic.plot(dataset, 
               title=FALSE, 
               scale.bar=TRUE, 
               mm.grid=FALSE, 
               pch=21, 
               col=grey(0.1), 
               dev.size=c(13.54595, 10.65946),
               region.colors = F
)

### input dataset from *.csv
dataset <- read.csv("5406_2_1_2_regi.csv")

###
rstudioapi::restartSession()
###
#stitch multiple sections
folder<-'D:2020 RV projection/wholebrain/RV SC no in situ/5432'
stitch.animal(folder, FFC=TRUE, web.map=FALSE) #, rotate = 90
get.atlas.image(-3.4, plane='coronal', save.image = FALSE, close.image = FALSE)