if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISl_data/obj.data cfg/yolov3-tiny-isl.cfg backup/yolov3-tiny-isl_final.weights < ISl_data/test.txt > results/Yolov3-Tiny-isl_test_cpu_results.txt
else
    ./darknet detector test ISl_data/obj.data cfg/yolov3-tiny-isl.cfg backup/yolov3-tiny-isl_final.weights < ISl_data/test.txt > results/Yolov3-Tiny-isl_test_results.txt
fi
