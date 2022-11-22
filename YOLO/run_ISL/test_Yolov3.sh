if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISl_data/obj.data cfg/yolov3-isl.cfg backup/yolov3-isl_final.weights < ISl_data/test.txt > results/Yolov3-isl_test_cpu_results.txt
else
    ./darknet detector test ISl_data/obj.data cfg/yolov3-isl.cfg backup/yolov3-isl_final.weights < ISl_data/test.txt > results/Yolov3-isl_test_results.txt
fi
