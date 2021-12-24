(declaim (optimize (safety 0) (debug 0) (speed 3)))

(defun fac (n)
  (declare (fixnum n))
  (labels ((rec (n acc)
             (declare (fixnum n))
             (if (> n 1)
                 (rec (1- n) (* n acc))
                 acc)))
    (rec (1- n) n)))

(defun main ()
  (let ((tests (read)))
    (declare (fixnum tests))
    (mapcar #'print
            (loop for i from 1 to tests collect (fac (read))))))

(main)
