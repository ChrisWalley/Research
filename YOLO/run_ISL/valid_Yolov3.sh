if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISL_data/obj.data cfg/yolov3-isl.cfg backup/yolov3-isl_final.weights < ISL_data/valid.txt > results/Yolov3-isl_valid_cpu_results.txt
else
    ./darknet detector test ISL_data/obj.data cfg/yolov3-isl.cfg backup/yolov3-isl_final.weights < ISL_data/valid.txt > results/Yolov3-isl_valid_results.txt
fi
