if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISL_data/obj.data cfg/yolov3-tiny-isl.cfg backup/yolov3-tiny-isl_final.weights < ISL_data/valid.txt > results/Yolov3-Tiny-isl_valid_cpu_results.txt
else
    ./darknet detector test ISL_data/obj.data cfg/yolov3-tiny-isl.cfg backup/yolov3-tiny-isl_final.weights < ISL_data/valid.txt > results/Yolov3-Tiny-isl_valid_results.txt
fi
