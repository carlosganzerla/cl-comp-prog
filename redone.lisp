(declaim (optimize (safety 0) (debug 0) (speed 3)))

(defconstant +size+ 1000000)

(defmacro with-gensyms (syms &body body)
  `(let (,@(mapcar (lambda (s) `(,s (gensym))) syms))
     ,@body))

(defmacro for ((var from to &optional result) &body body)
  (with-gensyms (%from %to)
                `(let ((,%from ,from) (,%to ,to))
                   (do ((,var ,%from (1+ ,var)))
                       ((>= ,var ,%to) ,result)
                       (declare (fixnum ,var ,%from ,%to))
                       ,@body))))

(defun get-sums ()
  (let ((vec (make-array +size+ :element-type 'fixnum)))
    (declare ((array fixnum) vec))
    (for (i 0 +size+)
         (setf (aref vec i) (1+ i)))
    (for (i 1 +size+ vec) 
         (let ((prev (aref vec (1- i)))
               (current (aref vec i)))
           (setf (aref vec i) 
                 (mod (+ prev current (* prev current)) 1000000007))))))


(defun main ()
  (let ((n (read)) (answers (get-sums)))
    (declare (fixnum n))
    (mapc #'print
          (loop for i from 1 to n collect (aref answers (1- (read)))))))
