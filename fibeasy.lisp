(defun fib (n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (t (do ((prev 0)
                (current 1)
                (idx 1 (1+ idx)))
               ((>= idx n) current)
               (psetf current (+ prev current) prev current)))))

(defun main ()
  (dotimes (x (read))
    (print (mod (fib (1- (expt 2 (floor (log (read) 2))))) 10))))

(dotimes (x 30)
  (print (fib (* 10 x))))

(dotimes (x 30)
  (format t "~A ~A~%" (fib x) (fib-10 x)))

(dotimes (x 30)
  (print (fib-10 30)))


(typep 576460752303423488 '(integer 0 1000000000000000000))

(print (mod (fib (1- (expt 2 (floor (log 1000000000000000000 2))))) 10))


(defvar *pattern-10* #(0 5 5))
(defvar *pattern-11* #(1 9 6 9 1 4))
(defvar *pattern-12* #(1 4 1 9 6 9))
(defvar *pattern-12* #(2 3 7 8 7 3))

(defun fib-10 (n)
  
  (let ((mod10 (mod n 10))
        (div10 (floor (/ n 10))))
    (do ((prev ())))
    )
  )

(defun fib-10 (n)
  (declare ((integer 0 1000000000000000000) n))
  (let ((pattern (case (mod n 10)
                   (0 #(0 5 5))
                   (1 #(1 9 6 9 1 4))
                   (2 #(1 4 1 9 6 9))
                   (3 #(2 3 7 8 7 3))
                   (4 #(3 7 8 7 3 2)) 
                   (5 #(5 0 5))
                   (6 #(8 7 3 2 3 7))
                   (7 #(3 7 8 7 3 2))
                   (8 #(1 4 1 9 6 9))
                   (9 #(4 1 9 6 9 1))
                   (t (error "Not good")))))
    (aref pattern (mod (floor (/ n 10)) (length pattern)))))

