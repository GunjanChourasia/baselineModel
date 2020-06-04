import os
import shutil
files = [x for x in os.listdir("./nut_snacks/dataset")]
train_file = open("./nut_snacks/train_data.txt","a")
test_file = open("./nut_snacks/test_data.txt","a")

if os.path.isdir(os.path.join(os.getcwd(),"nut_snacks/train")):
    train_dir=os.path.join(os.getcwd(),"nut_snacks/train")
else:
    os.mkdir(os.path.join(os.getcwd(),"nut_snacks/train"))
    train_dir=os.path.join(os.getcwd(),"nut_snacks/train")

if os.path.isdir(os.path.join(os.getcwd(),"nut_snacks/val")):
    test_dir=os.path.join(os.getcwd(),"nut_snacks/val")
else:
    os.mkdir(os.path.join(os.getcwd(),"nut_snacks/val"))
    test_dir=os.path.join(os.getcwd(),"nut_snacks/val")

print (files)
for j,file in enumerate(sorted(files)):
    img_list = [x for x in os.listdir("./nut_snacks/dataset/"+str(file)) if x.endswith(".jpg")]
    for i, img_name in enumerate(sorted(img_list)):
        txt = str(img_name)+"~"+str(file)
        if len(img_list)==1:
            os.mkdir(test_dir+"/{}".format(str(j)))
            os.mkdir(train_dir+"/{}".format(str(j)))
            shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),test_dir+"/{}".format(str(j)))
            shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),train_dir+"/{}".format(str(j)))

        elif i%4==0:
            if os.path.isdir(test_dir+"/{}".format(str(j))):
                shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),test_dir+"/{}".format(str(j)))
            else:
                os.mkdir(test_dir+"/{}".format(str(j)))
                shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),test_dir+"/{}".format(str(j)))
            test_file.write(txt+"\n")
        else:
            if os.path.isdir(train_dir+"/{}".format(str(j))):
                shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),train_dir+"/{}".format(str(j)))
            else:
                os.mkdir(train_dir+"/{}".format(str(j)))
                shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),train_dir+"/{}".format(str(j)))

            train_file.write(txt+"\n")
            
train_file.close()
test_file.close()